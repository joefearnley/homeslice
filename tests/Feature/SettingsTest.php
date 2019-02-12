<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use App\User;

class SettingsTest extends TestCase
{
    use DatabaseMigrations;

    public function testRedirectedToLoginPageWhenNotLoggedIn()
    {
        $this->get('/settings')
            ->assertRedirect('/login');
    }

    public function testShowsSettingsPage()
    {
        $user = factory(User::class)->create();

        $this->actingAs($user)
            ->get('/settings')
            ->assertStatus(200)
            ->assertSee($user->name)
            ->assertSee($user->email)
            ->assertSee($user->username);
    }

    public function testUpdatesUserSettings()
    {
        $user = factory(User::class)->create();
        $oldName = $user->name;
        $oldUsername = $user->username;

        $formData = [
            'name' => 'Joe Fearnley',
            'username' => 'joefearnley',
            'email' => 'joe.fearnley@gmail.com'
        ];

        $this->actingAs($user)
            ->post('/settings/save', $formData)
            ->assertStatus(302);

        $updatedUser = User::find($user->id);

        $this->assertFalse($oldName === $updatedUser->name);
        $this->assertFalse($oldUsername === $updatedUser->username);
    }

    public function testNameUsernameEmailAreRequired()
    {
        $user = factory(User::class)->create();

        $this->actingAs($user)
            ->post('/settings/save', [])
            ->assertStatus(302)
            ->assertSessionHasErrors([
                'name' => 'The name field is required.',
                'username' => 'The username field is required.',
                'email' => 'The email field is required.'
            ]);
    }
}

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

        $this->actingAs($user)
            ->post('/settings/save', [
                'name' => 'Joe Fearnley',
                'username' => 'joefearnley',
                'email' => 'joe.fearnley@gmail.com'
            ])
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

    public function testPasswordIsRequired()
    {
        $user = factory(User::class)->create();

        $this->actingAs($user)
            ->post('/settings/password/save', [])
            ->assertStatus(302)
            ->assertSessionHasErrors([
                'password' => 'The password field is required.'
            ]);
    }

    public function testPasswordsMustMatch()
    {
        $user = factory(User::class)->create();

        $this->actingAs($user)
            ->post('/settings/password/save', [
                'password' => '123456',
                'password_confirmation' => '1234567'
            ])
            ->assertStatus(302)
            ->assertSessionHasErrors([
                'password' => 'The password confirmation does not match.'
            ]);
    }

    public function testPasswordIsUpdated()
    {
        $oldPassword = 'password';
        $newPassword = 'secret';

        $user = factory(User::class)->create([
            'password' => \Hash::make($oldPassword)
        ]);

        $this->actingAs($user)
            ->post('/settings/password/save', [
                'password' => $newPassword,
                'password_confirmation' => $newPassword
            ])
            ->assertStatus(302);

        $user->refresh();
        $this->assertTrue(\Hash::check($newPassword, $user->password));
    }
}

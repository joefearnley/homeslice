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

    // update user settings

}

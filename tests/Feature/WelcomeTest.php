<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;
use App\Models\User;

class WelcomeTest extends TestCase
{
    use RefreshDatabase;

    public function testWelcomPageShouldDisplayAppName()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
        $response->assertViewIs('welcome');
        $response->assertSee('Homeslice - your bookmarking buddy.');
    }

    public function testWelcomPageShouldDisplayLoginRegister()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
        $response->assertSee('Login');
        $response->assertSee('Register');
    }

    public function testWelcomPageShouldRedirectToHomeWhenLoggedIn()
    {
        $user = User::factory()->create();

        $response = $this->actingAs($user)->get('/');
        $response->assertStatus(302);
        
        $response->assertRedirect('/home');
    }

}

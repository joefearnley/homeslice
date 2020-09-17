<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;
use App\Models\User;

class HomepageTest extends TestCase
{
    use RefreshDatabase;

    public function testHomepageShouldDisplayAppName()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
        $response->assertViewIs('welcome');
        $response->assertSee('Homeslice - your bookmarking buddy.');
    }

    public function testHomepageShouldDisplayLoginRegister()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
        $response->assertSee('Login');
        $response->assertSee('Register');
    }

    public function testHomepageShouldRedirectToHomeWhenLoggedIn()
    {
        $user = User::factory()->create();

        $response = $this->actingAs($user)->get('/');
        
        $response->assertRedirect('/home');
    }

}

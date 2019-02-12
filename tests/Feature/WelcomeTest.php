<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;
use App\User;

class WelcomePageTest extends TestCase
{
    use DatabaseMigrations;

    public function testShowHomePage()
    {
        $this->get('/')
            ->assertStatus(200)
            ->assertSee('HomeSlice')
            ->assertSee('Login')
            ->assertSee('Sign Up');
    }

    public function testShouldBeRedirectedToTheHomePageIfLoggedIn()
    {
        $user = factory(User::class)->create();
        $this->actingAs($user)
            ->get('/')
            ->assertRedirect('/home');
    }
}
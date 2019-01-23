<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;
use App\User;

class HomePageTest extends TestCase
{
    use DatabaseMigrations;

    public function testShowHomePage()
    {
        $this->get('/')
            ->assertStatus(200)
            ->assertSee('Home Slice')
            ->assertSee('Login')
            ->assertSee('Sign Up');
    }

    public function testHomePageShowsHomeLinkWhenUserIsLoggedIn()
    {
        $user = factory(User::class)->create();
        $this->actingAs($user)
            ->get('/')
            ->assertStatus(200)
            ->assertSee('Home')
            ->assertDontSee('Login');
    }
}

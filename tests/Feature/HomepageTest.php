<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class HomepageTest extends TestCase
{

    public function testHomepageShouldDisplayAppName()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
        $response->assertViewIs('home');
        $response->assertSee('Homeslice - your bookmarking buddy.');
    }

    public function testHomepageShouldDisplayLoginRegister()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
        $response->assertViewIs('home');
        $response->assertSee('Login');
        $response->assertSee('Register');
    }
}

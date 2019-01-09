<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class HomePageTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testShowHomePage()
    {
        $this->visit('/')
            ->see('Home Slice')
            ->see('Login')
            ->see('Sign Up');
    }
}

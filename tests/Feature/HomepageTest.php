<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;
use App\Models\User;

class HomepageTest extends TestCase
{
    use RefreshDatabase;

    protected $user = null;

    protected function setUp(): void
    {
        parent::setUp();

        $this->user = User::factory()->create();
    }

    public function testShouldRedirectToLoginIfNotAuthenticated()
    {
        $response = $this->get('/home');

        $response->assertStatus(302);

        $response->assertRedirect('/login');
    }

    public function testShouldSeeAccountLinkWhenAuthenticated()
    {
        $response = $this->actingAs($this->user)->get('/home');

        $response->assertStatus(200);
        $response->assertSeeText($this->user->name);
    }
}

<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;
use App\User;
use App\Post;

class PostTest extends TestCase
{
    use DatabaseMigrations;
    use RefreshDatabase;

    public function testShouldRedictToLoginWhenNotLoggedIn()
    {
        $this->get('/posts/create')
            ->assertRedirect('/login');
    }

    public function testCreatePostsShowsForm()
    {
        $user = factory(User::class)->create();
        $this->actingAs($user)
            ->get('/posts/create')
            ->assertStatus(200)
            ->assertSee('What are you going to say?')
            ->assertSee('Say something...');
    }

    public function testAddPost()
    {
        $user = factory(User::class)->create();
        $postData = [
            'body' => 'This is a post'
        ];

        $this->actingAs($user)
            ->post('/posts', $postData)
            ->assertRedirect('home');

        $this->assertDatabaseHas('posts', [
            'body' => 'This is a post'
        ]);
    }

    public function testBodyIsRequired()
    {
        $user = factory(User::class)->create();

        $this->actingAs($user)
            ->post('/posts', [])
            ->assertStatus(302)
            ->assertSessionHasErrors([
                'body' => 'The body field is required.'
            ]);
    }
}

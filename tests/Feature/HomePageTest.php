<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;
use App\User;
use App\Post;

class HomePageTest extends TestCase
{
    use DatabaseMigrations;

    public function testHomePageRedirectsToWelcomePageIfNotLoggedIn()
    {
        $this->get('/home')
            ->assertRedirect('/login');
    }

    public function testHomePageShowsPosts()
    {
        $user = factory(User::class)->create();

        // insert some posts
        $post1 = factory(Post::class)->create([ 'user_id' => $user->id ]);
        $post2 = factory(Post::class)->create([ 'user_id' => $user->id ]);
        $post3 = factory(Post::class)->create([ 'user_id' => $user->id ]);

        // call /feed
        $this->actingAs($user)
            ->get('/home')
            ->assertSee(e($post1->body))
            ->assertSee(e($post2->body))
            ->assertSee(e($post3->body));
    }
}

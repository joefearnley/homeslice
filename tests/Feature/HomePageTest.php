<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
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

    public function testHomePageShowsMessageWhenThereAreNoPosts()
    {
        $user = factory(User::class)->create();

        $this->actingAs($user)
            ->get('/home')
            ->assertSee(e('You have not created any posts yet.'))
            ->assertSee(e('Click on the Add Post button to get started.'));
    }

    public function testHomePageShowsPosts()
    {
        $user = factory(User::class)->create();

        $post1 = factory(Post::class)->create([ 'user_id' => $user->id ]);
        $post2 = factory(Post::class)->create([ 'user_id' => $user->id ]);
        $post3 = factory(Post::class)->create([ 'user_id' => $user->id ]);

        $this->actingAs($user)
            ->get('/home')
            ->assertSee(e($post1->body))
            ->assertSee(e($post2->body))
            ->assertSee(e($post3->body));
    }
}

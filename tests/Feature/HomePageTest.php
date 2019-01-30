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

    public function testHomePageShowsMessageIfNoPostsHaveBeenCreated()
    {
        $this->assertTrue(true);
    }

    // public function testHomePageShowsPosts()
    // {
    //     $user = factory(User::class)->create();

    //     // insert some posts
    //     $post1 = factory(Post::class)->create();
    //     $post2 = factory(Post::class)->create();
    //     $post3 = factory(Post::class)->create();

    //     // call /feed
    //     $this->actingAs($user)
    //         ->get('/home')

    //     // assert there are posts being shown in feed
    // }
}

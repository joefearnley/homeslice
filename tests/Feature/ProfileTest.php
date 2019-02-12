<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use App\User;
use App\Post;

class ProfileTest extends TestCase
{
    use DatabaseMigrations;

    public function testProfileShowsMessageWhenNoPosts()
    {
        $user = factory(User::class)->create([
            'name' => 'John Doe',
            'username' => 'johndoe123'
        ]);

        $this->get('/johndoe123')
            ->assertSee($user->username . ' has not posted anything yet');
    }

    public function testProfileShowsPosts()
    {
        $user = factory(User::class)->create([
            'name' => 'John Doe',
            'username' => 'johndoe123'
        ]);

        $post1 = factory(Post::class)->create(['user_id' => $user->id]);
        $post2 = factory(Post::class)->create(['user_id' => $user->id]);
        $post3 = factory(Post::class)->create(['user_id' => $user->id]);

        $this->get('/johndoe123')
            ->assertSee($user->username)
            ->assertSee(e($post1->body))
            ->assertSee($post1->display_date)
            ->assertSee(e($post2->body))
            ->assertSee($post2->display_date)
            ->assertSee(e($post3->body))
            ->assertSee($post3->display_date);
    }
}

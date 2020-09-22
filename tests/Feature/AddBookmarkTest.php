<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class AddBookmarkTest extends TestCase
{
    public function testAddBookmarkPageLoads()
    {
        $response = $this->get('/bookmark/add');

        $response->assertStatus(200);
    }
}

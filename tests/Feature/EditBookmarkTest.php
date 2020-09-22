<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class EditBookmarkTest extends TestCase
{

    public function testEditBookmarkPageLoads()
    {
        $response = $this->get('/bookmark/edit');

        $response->assertStatus(200);
    }
}

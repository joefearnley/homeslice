<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;

class FeedController extends Controller
{
    public function index()
    {
        // fetch posts
        $posts = User::posts();

        // return posts view
        return view('feed', $posts);
    }

}

<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;
use App\Post;

class ProfileController extends Controller
{
    public function index($username)
    {
        $user = User::where('username', $username)->first();

        if (empty($user)) {
            abort(404);
        }

        return view('profile')
            ->with('user', $user)
            ->with('posts', $user->posts);
    }
}

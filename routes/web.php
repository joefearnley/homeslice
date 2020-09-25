<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\BookmarkController;

Route::get('/', [WelcomeController::class, 'index']);

Route::middleware(['auth:sanctum', 'verified'])
    ->get('/home', [HomeController::class, 'index'])
    ->name('home');


Route::get('/bookmark/add', [BookmarkController::class, 'create'])->name('add-bookmark');
Route::post('/bookmark/add', [BookmarkController::class, 'store']);
Route::get('/bookmark/edit', [BookmarkController::class, 'edit'])->name('edit-bookmark');
Route::post('/bookmark/update', [BookmarkController::class, 'update']);

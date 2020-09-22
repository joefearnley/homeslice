<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\BookmarkController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', [WelcomeController::class, 'index']);

// Route::get('/home', [HomeController::class, 'index']);


Route::middleware(['auth:sanctum', 'verified'])
    ->get('/home', [HomeController::class, 'index'])
    ->name('home');


Route::get('/bookmark/add', [BookmarkController::class, 'create'])->name('add-bookmark');
Route::post('/bookmark/add', [BookmarkController::class, 'store']);
Route::get('/bookmark/edit', [BookmarkController::class, 'edit'])->name('edit-bookmark');
Route::post('/bookmark/update', [BookmarkController::class, 'update']);

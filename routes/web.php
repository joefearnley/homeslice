<?php

Route::get('/', 'WelcomeController@index');

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');
Route::get('/settings', 'SettingsController@index')->name('settings');
Route::post('/settings/save', 'SettingsController@update');
Route::post('/settings/password/save', 'SettingsController@updatePassword');

Route::resource('posts', 'PostController')->middleware('auth');

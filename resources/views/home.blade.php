@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2>Bong, Bong!</h2>
            @if ($posts->isEmpty())
                <h4 class="mt-5">
                    You have not created any posts yet.<br>
                    <small class="text-muted">Click on the Add Post button to get started.</small>
                </h4>
            @else
                @foreach ($posts as $post)
                    <div class="card mt-5">
                        <div class="card-header"><strong>joefearnley</strong> - Feb 7</div>
                        <div class="card-body">
                            {{ $post->body }}
                        </div>
                    </div>
                @endforeach
            @endif
        </div>
    </div>
</div>
@endsection

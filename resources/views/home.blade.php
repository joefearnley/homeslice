@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2>Bong, Bong!</h2>
            @foreach ($posts as $post)
                <div class="card mt-5">
                    <div class="card-header"><strong>joefearnley</strong> - Feb 7</div>
                    <div class="card-body">
                        {{ $post->body }}
                    </div>
                </div>
            @endforeach
        </div>
    </div>
</div>
@endsection

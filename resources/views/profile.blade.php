@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            @if ($posts->isEmpty())
                <h4 class="mt-5">{{ $user->username }} has not posted anything yet</h4>
            @else
                @foreach ($posts as $post)
                    <div class="card mt-5">
                        <div class="card-header"><strong>{{ $user->username }}</strong> - {{ $post->display_date }}</div>
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

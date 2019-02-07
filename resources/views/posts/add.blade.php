@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">What are you going to say?</div>
                <div class="card-body">
                    <form method="POST" action="/posts">
                        @csrf
                        <div class="mb-3">
                            <label for="body">Say something...</label>
                            <textarea class="form-control {{ $errors->has('body') ? 'is-invalid' :'' }}" name="body" id="body" placeholder="Write it here..."></textarea>
                            @if ($errors->any())
                            <div class="invalid-feedback">
                                Please say something.
                            </div>
                            @endif
                        </div>
                        <button type="submit" class="btn btn-primary">Say It!</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
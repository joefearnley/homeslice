@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">What are you going to say?</div>
                <div class="card-body">
                    <form>
                        <div class="form-group">
                            <label for="exampleFormControlTextarea1">Say something...</label>
                            <textarea class="form-control" id="posttext" rows="3"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Say It!</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
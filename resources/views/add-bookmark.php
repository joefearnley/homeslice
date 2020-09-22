<x-app-layout>
    <div class="py-12">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <div class="bg-white overflow-hidden shadow-xl sm:rounded-lg">
                <form method="POST" action="{{ route('add-bookmark') }}">
                @csrf

                <div>
                    <label for="name">
                        {{ __('Name') }}
                        <input class="block mt-1 w-full" type="text" name="name" :value="old('name')" required autofocus autocomplete="name" />
                    </label>
                </div>

                <div class="mt-4">
                    <x-jet-label value="{{ __('Url') }}" />
                    <x-jet-input class="block mt-1 w-full" type="email" name="email" :value="old('email')" required />
                </div>

                <div class="flex items-center justify-end mt-4">
                    <x-jet-button class="ml-4">
                        {{ __('Create') }}
                    </x-jet-button>
                </div>
            </form>
            </div>
        </div>
    </div>
</x-app-layout>
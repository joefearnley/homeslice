const Login = () => {

    const handleSubmit = (event) => {
        event.preventDefault();

        const data = JSON.stringify({
            email: event.target.email.value,
            password: event.target.password.value,
        });

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: data,
        };

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/login/`, options)
            .then(response => response.json())
            .then(response => {
                console.log(response);
            })
            .catch((error) => {
                console.log(error)
            });
    }

    return (
        <div>
            <div className="mt-24 text-center">
                <h2 className="text-4xl font-bold tracking-tight">Sign in into your account</h2>
                <span className="text-sm">or <a href="/signup" className="text-gray-500 hover:underline"> register a new account </a> </span>
            </div>
            <div className="my-2 mx-4 flex justify-center md:mx-0">
                <form className="w-full max-w-xl rounded-lg bg-white p-6" onSubmit={handleSubmit}>
                    <div className="-mx-3 mb-6 flex flex-wrap">
                        <div className="mb-6 w-full px-3 md:w-full">
                            <label className="mb-2 block text-xs font-bold tracking-wide text-gray-700" htmlFor="Password">Email address
                                <input type="text" name="username" id="username" className="block w-full appearance-none rounded-lg border border-gray-400 bg-white py-3 px-3 font-medium leading-tight text-gray-900 focus:outline-none" required />
                            </label>
                        </div>
                        <div className="mb-6 w-full px-3 md:w-full">
                            <label className="mb-2 block text-xs font-bold tracking-wide text-gray-700" htmlFor="Password">Password
                                <input type="password" name="password" id="password" className="block w-full appearance-none rounded-lg border border-gray-400 bg-white py-3 px-3 font-medium leading-tight text-gray-900 focus:outline-none" required />
                            </label>
                        </div>
                        <div className="mb-3 flex w-full items-center justify-between px-3">
                            <label htmlFor="remember" className="flex w-1/2 items-center cursor-pointer">
                                <input type="checkbox" name="remember" id="remember" className="mr-1 bg-white shadow" />
                                <span className="pt-1 text-sm text-gray-700">Remember Me</span>
                            </label>
                            <div className="w-1/2 text-right">
                                <a href="#" className="text-sm tracking-tight text-gray-500 hover:underline">Forget your password?</a>
                            </div>
                        </div>
                        <div className="mb-6 w-full px-3 md:w-full">
                            <button className="block w-full appearance-none rounded-lg border border-gray-200 bg-gray-600 py-3 px-3 font-bold leading-tight text-gray-100 hover:bg-gray-500 focus:border-gray-500 focus:bg-white focus:outline-none">Sign in</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Login
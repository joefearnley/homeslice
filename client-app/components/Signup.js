const Signup = () => {

    const handleSubmit = (event) => {
        event.preventDefault();

        const data = JSON.stringify({
            username: event.target.username.value,
            email: event.target.email.value,
            password: event.target.password.value,
        });

        console.log(`data to be submitted`);
        console.log(data);

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: data,
        };

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/signup/`, options)
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
                <h2 className="text-4xl font-bold tracking-tight">Create Account</h2>
                <span className="text-sm">or <a href="#" className="text-gray-500 hover:underline"> register a new account </a> </span>
            </div>
            <div className="my-2 mx-4 flex justify-center md:mx-0">
                <form className="w-full max-w-xl rounded-lg bg-white p-6" onSubmit={handleSubmit}>
                    <div className="-mx-3 mb-6 flex flex-wrap">
                        <div className="mb-6 w-full px-3 md:w-full">
                            <label className="mb-2 block text-xs font-bold tracking-wide text-gray-700" htmlFor="Password">Username
                                <input type="text" name="username" id="username" placeholder="@username" className="block w-full appearance-none rounded-lg border border-gray-400 bg-white py-3 px-3 font-medium leading-tight text-gray-900 focus:outline-none" required />
                            </label>
                        </div>
                        <div className="mb-6 w-full px-3 md:w-full">
                            <label className="mb-2 block text-xs font-bold tracking-wide text-gray-700" htmlFor="Password">Email address
                                <input type="email" name="email" id="email"  placeholder="Email Address" className="block w-full appearance-none rounded-lg border border-gray-400 bg-white py-3 px-3 font-medium leading-tight text-gray-900 focus:outline-none" required />
                            </label>
                        </div>
                        <div className="mb-6 w-full px-3 md:w-full">
                            <label className="mb-2 block text-xs font-bold tracking-wide text-gray-700" htmlFor="Password">Password
                                <input type="password" name="password" id="password" placeholder="Password" className="block w-full appearance-none rounded-lg border border-gray-400 bg-white py-3 px-3 font-medium leading-tight text-gray-900 focus:outline-none" required />
                            </label>
                        </div>
                        <div className="mb-2 flex w-full items-center justify-between px-3">
                            <div className="mb-6 w-full px-3 md:w-full">
                                <button className="block w-full appearance-none rounded-lg border border-gray-200 bg-gray-600 py-3 px-3 font-bold leading-tight text-gray-100">Create Account</button>
                            </div>
                        </div>
                        <div className="flex w-full">
                            <div className="w-full text-center">
                                Alread have an account? <a href="/login" className="tracking-tight text-gray-500 hover:underline">Login</a>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Signup
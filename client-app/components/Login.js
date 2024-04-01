import { useRouter } from 'next/router'

const Login = () => {
    const router = useRouter();

    const handleSubmit = (event) => {
        event.preventDefault();

        const formData = new FormData(event.currentTarget)
        const username = formData.get('username');
        const password = formData.get('password');
        const remember_me = formData.get('remember');

        const bodyData = JSON.stringify({
            username,
            password,
            remember_me,
        });

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: bodyData,
        };

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/login/`, options)
            .then(response => response.json())
            .then(response => {
                
                router.push('/dashboard');
            })
            .catch((error) => {
                console.log(error);
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
                            <label className="mb-2 block text-xs font-bold tracking-wide text-gray-700" htmlFor="Password">Username
                                <input type="text" name="username" id="username" placeholder="@username" className="block w-full appearance-none rounded-lg border border-gray-400 bg-white py-3 px-3 font-medium leading-tight text-gray-900 focus:outline-none" required />
                            </label>
                        </div>
                        <div className="mb-6 w-full px-3 md:w-full">
                            <label className="mb-2 block text-xs font-bold tracking-wide text-gray-700" htmlFor="Password">Password
                                <input type="password" name="password" id="password" placeholder="Password" className="block w-full appearance-none rounded-lg border border-gray-400 bg-white py-3 px-3 font-medium leading-tight text-gray-900 focus:outline-none" required />
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
                            <button className="inline-block cursor-pointer rounded-md bg-gray-800 px-4 py-3 text-center text-sm font-semibold text-white transition duration-200 ease-in-out hover:bg-gray-900">Sign in</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Login
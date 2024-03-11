import { useRouter } from 'next/router'

const Signup = () => {
    const router = useRouter()

    const handleSubmit = (event) => {
        event.preventDefault();

        const formData = new FormData(event.currentTarget)
        const username = formData.get('username');
        const email = formData.get('email');
        const password = formData.get('password');

        const bodyData = JSON.stringify({
            username,
            email,
            password,
        });

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: bodyData,
        };

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/signup/`, options)
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
                <h2 className="text-4xl font-bold tracking-tight">Create Account</h2>
                <span className="text-sm">Alread have an account? <a href="/login" className="text-gray-500 hover:underline">Sign In</a> </span>
            </div>
            <div className="my-2 mx-4 flex justify-center md:mx-0">
                <form className="w-full max-w-xl rounded-lg bg-white p-6" onSubmit={handleSubmit}>
                    <div className="-mx-3 mb-6 flex flex-wrap">
                        <div className="mb-6 w-full px-3 md:w-full">
                            <label className="input input-bordered flex items-center gap-2">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" /></svg>
                                <input type="text" name="username" id="username" class="grow" placeholder="@username" required />
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
                            <button className="inline-block cursor-pointer rounded-md bg-gray-800 px-4 py-3 text-center text-sm font-semibold text-white transition duration-200 ease-in-out hover:bg-gray-900">Create Account</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Signup
import { useRouter } from 'next/router'
import Link from 'next/link';

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
            <div className="hero min-h-screen">
                <div className="hero-content flex-col w-full">
                    <h1 className="text-5xl font-bold flex gap-3 mb-8">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-12 h-12">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M10.5 6a7.5 7.5 0 1 0 7.5 7.5h-7.5V6Z" />
                            <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0 0 13.5 3v7.5Z" />
                        </svg>
                        <Link href="/">Homeslice</Link>
                    </h1>
                    <div className="text-center mb-2">
                        <h2 className="text-4xl font-bold tracking-tight mb-4">Create Account</h2>
                        <span className="text-sm">Alread have an account? <a href="/login" className="text-gray-500 hover:underline">Sign In</a> </span>
                    </div>
                    <div className="my-2 w-full md:w-1/3">
                        <form onSubmit={handleSubmit}>
                            <div className="mb-5">
                                <label htmlFor="username">Username</label>
                                <div className="mt-2">
                                    <input type="text" placeholder="@username" id="username" name="username" className="input input-bordered w-full" />
                                </div>
                            </div>
                            <div className="mb-5">
                                <label htmlFor="email">Email Address</label>
                                <div className="mt-2">
                                    <input type="email" placeholder="name@email.com" id="email" name="email" className="input input-bordered w-full" />
                                </div>
                            </div>
                            <div className="mb-5">
                                <label htmlFor="username">Password</label>
                                <div className="mt-2">
                                    <input type="password" placeholder="password" id="password" name="password" className="input input-bordered w-full" />
                                </div>
                            </div>
                            <button type="submit" className="btn btn-primary">
                                Sign up
                            </button>
                        </form>
                    </div>
                    </div>
                    </div>
        </div>
    )
}

export default Signup
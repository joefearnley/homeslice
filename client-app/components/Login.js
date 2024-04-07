import { useRouter } from 'next/router'
import { setCookie } from 'cookies-next';

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
                setCookie('homeslice_auth_token', response.token, {
                    maxAge: 60 * 60 * 24 * 7,
                    path: '/',
                });
                
                router.push('/dashboard');
            })
            .catch((error) => {
                console.log(error);
            });
    }

    return (
        <div>
            <div className="mt-24 text-center mb-8">
                <h2 className="text-4xl font-bold tracking-tight mb-4">Sign in into your account</h2>
                <span className="text-sm">or <a href="/signup" className="text-gray-500 hover:underline"> register a new account </a> </span>
            </div>
            <div className="my-2 mx-4 flex justify-center md:mx-0">
                <form className="w-full md:w-1/3" onSubmit={handleSubmit}>
                    <div className="mb-5">
                        <label htmlFor="username">Username</label>
                        <div className="mt-3">
                            <input type="text" placeholder="@username" id="username" name="username" className="input input-bordered w-full" />
                        </div>
                    </div>
                    <div className="mb-5">
                        <label htmlFor="username">Password</label>
                        <div className="mt-3">
                            <input type="password" placeholder="password" id="password" name="password" className="input input-bordered w-full" />
                        </div>
                    </div>
                    <button type="submit" className="btn btn-primary">
                        Sign in
                    </button>
                </form>
            </div>
        </div>
    )
}

export default Login
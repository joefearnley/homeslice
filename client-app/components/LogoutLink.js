import { useRouter } from 'next/router'

const LogoutLink = () => {
    const router = useRouter();

    const logout = (event) => {
        event.preventDefault();

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/logout/`)
            .then(response => response.json())
            .then(response => {
                console.log(response);
                router.push('/');
            })
            .catch((error) => {
                console.log(error);
            });
    }

    return (
        <a onClick={logout}>
            Logout
        </a>
    )
}

export default LogoutLink
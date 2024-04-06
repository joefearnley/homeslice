import { useRouter } from 'next/router'
import { getCookie, deleteCookie } from 'cookies-next';

const LogoutLink = () => {
    const router = useRouter();

    const logout = (event) => {
        event.preventDefault();

        const authToken = getCookie('homeslice_auth_token');
        const options = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${authToken}`,
            },
        };

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/logout/`, options)
            .then(response => response.json())
            .then(response => {
                deleteCookie('homeslice_auth_token');
                router.push('/');
            })
            .catch((error) => {
                console.log(error);
            });
    }

    return (
        <a onClick={logout}>
            Sign Out
        </a>
    )
}

export default LogoutLink
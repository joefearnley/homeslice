import RootLayout from '../components/RootLayout';
import Navbar from './Navbar';
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { hasCookie, getCookie } from 'cookies-next';
 
const AuthLayout = ({ children }) => {
    const router = useRouter();

    useEffect(() => {
        if (!hasCookie('homeslice_auth_token')) {
            router.replace('/');
            return;
        }
    }, [router]);

    return (
        <div>
            <RootLayout>
                <div className="container m-auto">
                    <Navbar />
                    <div className="p-5">
                        {children}
                    </div>
                </div>
            </RootLayout>
        </div>
    );
}

export default AuthLayout;
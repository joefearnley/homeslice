import RootLayout from '../components/RootLayout';
import Navbar from './Navbar'
 
const AuthLayout = ({ children }) => {
    return (
        <div>
            <RootLayout>
                <div className="container m-auto bg-base-100">
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
import AuthLayout from '../../components/AuthLayout';
import React, { useState, useEffect } from 'react';

const AccountSettings = () => {

    const [isLoading, setIsLoading] = useState(false);
    const [showAlert, setShowAlert] = useState(false);
    const [user, setUser] = useState({});
    const authToken = getCookie('homeslice_auth_token');

    useEffect(() => {
        
    }, [authToken]);

    return (
        <div className="pt-3">
            <article className="prose">
                <h1 className="pb-8">Account Settings</h1>
            </article>
            <div className="border p-5 w-1/2">
                <div role="alert" className={`alert alert-success mt-5 mb-8 ${ showAlert ? 'block' : 'hidden' }`}>
                    <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <span>Your information has been udpated!</span>
                </div>
                <article className="prose mb-5">
                    <h2>My Information</h2>
                </article>
                <form>
                    <div className="mb-5">
                        <label htmlFor="username">Username</label>
                        <div className="mt-3">
                            <input type="text" placeholder="@username" id="username" name="username" className="input input-bordered w-full max-w-xs" />
                        </div>
                    </div>
                    <div className="mb-5">
                        <label htmlFor="firstname">First Name</label>
                        <div className="mt-3">
                            <input type="text" placeholder="first name" id="firstname" name="firstname" className="input input-bordered w-full max-w-xs" />
                        </div>
                    </div>
                    <div className="mb-5">
                        <label htmlFor="lastname">Last Name</label>
                        <div className="mt-3">
                            <input type="text" placeholder="last name" id="lastname" name="lastname" className="input input-bordered w-full max-w-xs" />
                        </div>
                    </div>
                    <div className="mb-5">
                        <label htmlFor="email">Email Address</label>
                        <div className="mt-3">
                            <input type="email" placeholder="name@email.com" id="email" name="email" className="input input-bordered w-full max-w-xs" />
                        </div>
                    </div>
                    <button type="submit" className="btn">Save</button>
                </form>
            </div>
        </div>
    )
}

AccountSettings.getLayout = (page) => (
    <AuthLayout>{page}</AuthLayout>
);

export default AccountSettings;

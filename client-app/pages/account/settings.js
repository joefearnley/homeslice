import AuthLayout from '../../components/AuthLayout';
import React, { useState, useEffect } from 'react';
import { getCookie } from 'cookies-next';

const AccountSettings = () => {

    const [isLoading, setIsLoading] = useState(false);
    const [showAlert, setShowAlert] = useState(false);
    const [user, setUser] = useState({});
    const authToken = getCookie('homeslice_auth_token');

    const handleChange = (event) => {
        const { target } = event;
        setUser((prevState) => ({
            ...prevState,
            [target.name]: target.value,
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        console.log(user);

        const bodyData = JSON.stringify({
            username: user.username,
            first_name: user.first_name,
            last_name: user.last_name,
            email: user.email,
        });

        const options = {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${authToken}`,
            },
            body: bodyData,
        };

        console.log(options);

        fetch(`${user.url}`, options)
            .then(response => response.json())
            .then(response => {
                console.log(response);
                setShowAlert(true);
            })
            .catch((error) => {
                console.log(error);
            });
    };

    useEffect(() => {
        const options = {
            method: 'GET',
            headers: {
                'Authorization': `Token ${authToken}`,
            },
        };

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/accounts/`, options)
            .then(response => response.json())
            .then(response => {
                setUser(response[0]);
            })
            .catch((error) => {
                console.log(error);
            });
    }, [authToken, setUser]);

    return (
        <div className="pt-3">
            <article className="prose">
                <h1 className="pb-8">Account Settings</h1>
            </article>
            <div className="border p-5 w-full md:w-1/2">
                <div role="alert" className={`alert alert-success mt-5 mb-8 ${ showAlert ? 'block' : 'hidden' }`}>
                    <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <span>Your information has been udpated!</span>
                </div>
                <article className="prose mb-5">
                    <h2>My Information</h2>
                </article>
                <form onSubmit={handleSubmit}>
                    <div className="mb-5">
                        <label htmlFor="username">Username</label>
                        <div className="mt-3">
                            <input type="text" value={ user.username || '' } onChange={handleChange} placeholder="@username" id="username" name="username" className="input input-bordered w-full" />
                        </div>
                    </div>
                    <div className="mb-5">
                        <label htmlFor="firstname">First Name</label>
                        <div className="mt-3">
                            <input type="text" value={ user.first_name || ''} onChange={handleChange} placeholder="first name" id="first_name" name="first_name" className="input input-bordered w-full" />
                        </div>
                    </div>
                    <div className="mb-5">
                        <label htmlFor="lastname">Last Name</label>
                        <div className="mt-3">
                            <input type="text" value={ user.last_name || '' } onChange={handleChange} placeholder="last name" id="lastname" name="last_name" className="input input-bordered w-full" />
                        </div>
                    </div>
                    <div className="mb-5">
                        <label htmlFor="email">Email Address</label>
                        <div className="mt-3">
                            <input type="email" placeholder="name@email.com" onChange={handleChange} value={ user.email || '' }  id="email" name="email" className="input input-bordered w-full" />
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

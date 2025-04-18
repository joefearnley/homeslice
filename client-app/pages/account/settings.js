import AuthLayout from '../../components/AuthLayout';
import React, { useState, useEffect } from 'react';
import { getCookie, deleteCookie } from 'cookies-next';

const AccountSettings = () => {
    const [isLoadingInfo, setIsLoadingInfo] = useState(false);
    const [isLoadingPassword, setIsLoadingPassword] = useState(false);
    const [showInfoAlert, setShowInfoAlert] = useState(false);
    const [showPasswordAlert, setShowPasswordAlert] = useState(false);
    const [user, setUser] = useState({});
    const authToken = getCookie('homeslice_auth_token');

    const handleChange = (event) => {
        const { target } = event;
        setUser((prevState) => ({
            ...prevState,
            [target.name]: target.value,
        }));
    };

    const handleInfoFormSubmit = (event) => {
        event.preventDefault();
        setIsLoadingInfo(true);

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

        fetch(`${user.url}`, options)
            .then(response => response.json())
            .then(response => {
                setShowInfoAlert(true);
                setIsLoadingInfo(false);
            })
            .catch((error) => {
                console.log(error);
            });
    };

    const handlePasswordFormSubmit = (event) => {
        event.preventDefault();

        setIsLoadingPassword(true);

        console.log(event.currentTarget);

        const formData = new FormData(event.currentTarget)
        const password = formData.get('password');
        const confirmPassword = formData.get('confirm_password');

        console.log(formData.get('password'));

        const bodyData = JSON.stringify({
            password,
            confirmPassword,
        });

        console.log(bodyData);

        const options = {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${authToken}`,
            },
            body: bodyData,
        };

        fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/account/update-password/`, options)
            .then(response => response.json())
            .then(response => {

                console.log(response);

                // deleteCookie('homeslice_auth_token');
                // setCookie('homeslice_auth_token', response.token, {
                //     maxAge: 60 * 60 * 24 * 7,
                //     path: '/',
                // });

                setShowPasswordAlert(true);
                setIsLoadingPassword(false);
            })
            .catch((error) => {
                console.log(error);
            });
    };

    const deleteAccountSubmit = (event) => {
        event.preventDefault();
        setIsLoading(true);

        const options = {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${authToken}`,
            },
        };

        fetch(`${user.url}`, options)
            .then(response => response.json())
            .then(response => {
                setIsLoading(false);
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

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="border rounded-md p-5 w-full">
                    <div role="alert" className={`alert alert-success mt-5 mb-8 ${ showInfoAlert ? '' : 'hidden' }`}>
                        <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        <span>Your information has been udpated!</span>
                    </div>
                    <article className="prose mb-5">
                        <h2>My Information</h2>
                    </article>
                    <form onSubmit={handleInfoFormSubmit}>
                        <div className="mb-5">
                            <label htmlFor="username">Username</label>
                            <div className="mt-2">
                                <input type="text" value={ user.username || '' } onChange={handleChange} placeholder="@username" id="username" name="username" className="input input-bordered w-full" />
                            </div>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="firstname">First Name</label>
                            <div className="mt-2">
                                <input type="text" value={ user.first_name || ''} onChange={handleChange} placeholder="first name" id="first_name" name="first_name" className="input input-bordered w-full" />
                            </div>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="lastname">Last Name</label>
                            <div className="mt-2">
                                <input type="text" value={ user.last_name || '' } onChange={handleChange} placeholder="last name" id="lastname" name="last_name" className="input input-bordered w-full" />
                            </div>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="email">Email Address</label>
                            <div className="mt-2">
                                <input type="email" placeholder="name@email.com" onChange={handleChange} value={ user.email || '' }  id="email" name="email" className="input input-bordered w-full" />
                            </div>
                        </div>
                        <button type="submit" className="btn btn-primary">
                            Submit
                            {isLoadingInfo ? <span className="loading loading-dots loading-sm"></span> : null}
                        </button>
                    </form>
                </div>
                <div className="border rounded-md p-5 mt-8 md:mt-0 w-full">
                    <div role="alert" className={`alert alert-success mt-5 mb-8 ${ showPasswordAlert ? '' : 'hidden' }`}>
                        <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        <span>Password has been udpated!</span>
                    </div>
                    <article className="prose mb-5">
                        <h2>Change Password</h2>
                    </article>
                    <form onSubmit={handlePasswordFormSubmit}>
                        <div className="mb-5">
                            <label htmlFor="firstname">New Password</label>
                            <div className="mt-2">
                                <input type="password" placeholder="new password" id="password" name="password" className="input input-bordered w-full" />
                            </div>
                        </div>
                        <div className="mb-5">
                            <label htmlFor="lastname">New Password (again)</label>
                            <div className="mt-2">
                                <input type="password" placeholder="new password (again)" id="confirm_password" name="confirm_password" className="input input-bordered w-full" />
                            </div>
                        </div>
                        <button type="submit" className="btn btn-primary">
                            Submit
                            {isLoadingPassword ? <span className="loading loading-dots loading-sm"></span> : null}
                        </button>
                    </form>
                </div>
            </div>

            <div className="border rounded-md p-5 mt-8 w-full md:w-1/2">
                <article className="prose mb-5">
                    <h2>Delete Account</h2>
                </article>
                <p className="mb-5">Delete links and along with all account information.</p>
                <button type="submit" className="btn btn-primary" onClick={()=>document.getElementById('delete-account-modal').showModal()}>
                    Delete
                </button>
                <dialog id="delete-account-modal" className="modal">
                    <div className="modal-box">
                        <form method="dialog">
                            <button className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>  
                        </form>
                        <h3 className="font-bold text-lg">Are you sure you want to delete your account?</h3>
                        <p className="py-4">Once you click <strong>Delete Account</strong>, all account resources and data will be deleted forever. Click <strong>Delete Account</strong> to proceed.</p>
                        <div className="modal-action">
                            <form method="dialog" onSubmit={deleteAccountSubmit}> 
                                <button type="submit" className="btn btn-error btn-wide">Delete Account</button>
                            </form>
                        </div>
                    </div>
                </dialog>
            </div>
        </div>
    )
}

AccountSettings.getLayout = (page) => (
    <AuthLayout>{page}</AuthLayout>
);

export default AccountSettings;

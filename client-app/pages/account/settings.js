import AuthLayout from '../../components/AuthLayout';

const AccountSettings = () => {
    return (
        <div className="pt-3">
            <h1>This is the Account Settings Page</h1>
        </div>
    )
}

AccountSettings.getLayout = (page) => (
    <AuthLayout>{page}</AuthLayout>
);

export default AccountSettings;

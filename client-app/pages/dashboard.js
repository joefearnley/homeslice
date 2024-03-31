import AuthLayout from '../components/AuthLayout';

const Dashboard = () => {
    return (
        <div className="pt-3">
            <h1>This is the Dashboard</h1>
        </div>
    )
}

Dashboard.getLayout = (page) => (
    <AuthLayout>{page}</AuthLayout>
);

export default Dashboard

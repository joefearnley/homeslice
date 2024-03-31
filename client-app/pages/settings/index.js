import AuthLayout from '../../components/AuthLayout';

const SetingsIndex = () => {
    return (
        <div className="pt-3">
            <h1>This is the Settings Index Page</h1>
        </div>
    )
}

SetingsIndex.getLayout = (page) => (
    <AuthLayout>{page}</AuthLayout>
);


export default SetingsIndex
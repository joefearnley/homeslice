import AuthLayout from '../../components/AuthLayout';

const LinksIndex = () => {
    return (
        <div className="pt-3">
            <h1>This is the Link Index Page</h1>
        </div>
    )
}

LinksIndex.getLayout = (page) => (
    <AuthLayout>{page}</AuthLayout>
);

export default LinksIndex;
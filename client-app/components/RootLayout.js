import Head from 'next/head';

const RootLayout = ({ children }) => {
    return (
        <div>
            <Head>
                <title>Homeslice</title>
                <meta name="description" content="All of your internet locations in one place." />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            {children}

            <footer>

            </footer>
        </div>
    );
};

export default RootLayout;
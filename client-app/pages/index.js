import Head from 'next/head'
import Image from 'next/image'

export default function Home() {
  return (
    <div className="bg-gray-50">
        <Head>
            <title>Homeslice</title>
            <meta name="description" content="All of your internet locations in one place." />
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className="container mx-auto">
            <div className="relative min-h-screen overflow-hidden py-6 sm:py-20">
                <div className="relative px-6 pt-10 pb-8 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
                    <div className="mx-auto max-w-md">
                        <div className="divide-y divide-gray-300/50">
                            <div className="space-y-6 py-8 text-base leading-7 text-gray-600 text-center">
                                <h1 className="text-7xl font-bold">Homeslice</h1>
                                <h3 className="text-lg">All of your internet locations in one place.</h3>
                                <div className="sm:flex flex-row justify-evenly pt-3 w-3/4 sm:w-full">
                                    <a href="/signup"  className="inline-block cursor-pointer rounded-md bg-gray-800 px-4 py-3 text-center text-sm font-semibold text-white transition duration-200 ease-in-out hover:bg-gray-900">Sign Up</a>
                                    <a href="/login" className="inline-block cursor-pointer rounded-md bg-gray-800 px-4 py-3 text-center text-sm font-semibold text-white transition duration-200 ease-in-out hover:bg-gray-900">Sign In</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <footer>

        </footer>
    </div>
  )
}

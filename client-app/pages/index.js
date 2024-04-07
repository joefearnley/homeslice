import Link from 'next/link';
import RootLayout from '../components/RootLayout';

export default function Home() {
  return (
    <div>
        <RootLayout>
            <div className="hero min-h-screen bg-base-200">
                <div className="hero-content text-center">
                    <div className="max-w-md">
                        <h1 className="text-5xl font-bold flex gap-3">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-12 h-12">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M10.5 6a7.5 7.5 0 1 0 7.5 7.5h-7.5V6Z" />
                                <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0 0 13.5 3v7.5Z" />
                            </svg>
                            <span>Homeslice</span>
                        </h1>
                        <p className="py-8">All of your internet locations in one place.</p>
                        <Link href="/signup"  className="btn btn-primary mr-4">Sign Up</Link>
                        <Link href="/login" className="btn btn-primary ml-4">Sign In</Link>
                    </div>
                </div>
            </div>       
        </RootLayout>
    </div>
  )
}

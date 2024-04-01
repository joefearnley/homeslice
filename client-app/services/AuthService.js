

const AuthService = () => {
    login: async (email, password) => {
        const { data: token } = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/login/`, options)
            .then(response => response.json())
            .then(response => {
                
            })
            .catch((error) => {
                console.log(error);
            });

        console.log(token);

        if (token) {
            console.log("Got token");
            Cookies.set("accessToken", token.access, { expires: 60 });
            api.defaults.headers.Authorization = `Bearer ${token.access}`;
            const { data: user } = await api.get("users/current/");
            console.log("Got user", user);

            return user;
        }
        },
    
};
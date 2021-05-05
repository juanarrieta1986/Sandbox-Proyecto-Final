const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			//Adde new for email sending START
			emailMsgTemplate: {
				SecureToken: "c1cad838-3de0-485d-955c-d71228c94cd4",
				To: "juanca86@gmail.com",
				From: "dirpro4g@gmail.com",
				Subject: "This is the subject",
				Body: "And this is the body"
			}
			//Adde new for email sending END
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: () => {
				// fetching data from the backend
				fetch(process.env.BACKEND_URL + "/api/hello")
					.then(resp => resp.json())
					.then(data => setStore({ message: data.message }))
					.catch(error => console.log("Error loading message from backend", error));
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			},
			//Adde new for email sending START
			sendEmail: () => {
				const store = getStore();
				console.log(store.emailMsgTemplate);
				Email.send(store.emailMsgTemplate).then(message => alert("mail sent successfully"));
				//return message;
				//setStore({ demo: demo });
			},
			addEmailScript: () => {
				let externalScript = document.createElement("script");
				externalScript.setAttribute("src", "https://smtpjs.com/v3/smtp.js");
				document.head.appendChild(externalScript);
			}
			//Adde new for email sending STOP
		}
	};
};

export default getState;

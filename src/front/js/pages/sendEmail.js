import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.scss";

export const SendEmail = () => {
	const { store, actions } = useContext(Context);

	return (
		<div>
			<script src="https://smtpjs.com/v3/smtp.js" />
			<input type="button" value="Send Email" onClick={() => actions.sendEmail()} />
		</div>
	);
};

$.ajax({
    url: '/check_reminders/', // This is the API endpoint
    method: 'GET',
    dataType: 'json',
    success: function (data) {
        // Handle the response data here
        if (data.hasReminder) {
            // Display the reminder popup using data.reminderText
            alert('Reminder: ' + data.reminderText);
        } else {
            // No reminders found
            console.log('No reminders found.');
        }
    },
    error: function () {
        // Handle any AJAX errors here
        console.error('An error occurred while checking reminders.');
    },
});

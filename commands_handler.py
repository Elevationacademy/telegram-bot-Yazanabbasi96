import functions


def command_parser(message):
    try:
        message_list = message.split()
        command = message_list[0][1:]
        number = int(message_list[1])
        return functions.functions_dict[command](number)
    except:
        return "Errrrorrrr"

MinionCmd
=========

CMD Loop Manager
===============================================

Official repo: <https://github.com/JoshuaEnglish/minioncmd>

Author email: <mailto://josh@joshuarenglish.com>

Tool for creating multi-level command line tools that allows switching between subcommands.

Sampe Code:

	class SubmissionCmd(MinionCmd):
        doc_leader = "Help for SubmissionCmd"

    class StoryCmd(MinionCmd):
        doc_leader = "Help for StoryCmd"

    class MarketCmd(MinionCmd):
        doc_leader = "Help for MarketCmd"

        def do_hello(self, line):
            print("Hello to '{}' from Market".format(line))
            self.master.cmdqueue.append('push hello from Market!')

    class App(BossCmd):
        doc_leader = "Help for the main application"

        def do_push(self, line):
            print("App pushes:", line)

    Boss = App()

    # long way to add minion to boss
    Story = StoryCmd('story')
    Boss.add_minion('story', Story)

    # minions accept a boss
    Submission = SubmissionCmd('submission', Boss)
    Market = MarketCmd('market', Boss)

    Boss.onecmd('story market hello onecmd')





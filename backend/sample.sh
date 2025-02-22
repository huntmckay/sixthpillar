sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from macrocycle'
echo ""
echo "---"
echo ""
sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from mesocycle'
echo ""
echo "---"
echo ""
sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from microcycle'
